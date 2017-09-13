from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode, Modifier
from menus.menu_pool import menu_pool

from blog.models import *
from cms.models import Page


class PostsMenu(CMSAttachMenu):
    name = _("PostMenu")

    def get_nodes(self,request):
        """
        This method is used to build the menu tree
        """
        nodes = []
        for post in Post.objects.all():
            node = NavigationNode(
                title = post.title,
                url = reverse('blog:post_detail', args=(post.pk,)),
                id = post.pk,
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(PostsMenu)


class PostModifier(Modifier):
    """
    This modifier makes the changed_by attribute of a page accessible for the menu system
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        #only do something when the menu has already been cut
        if post_cut:
            #only consider nodes that refer to cms pages
            #and put them in a dict for dfficient access
            page_nodes = {n.id: n for n in nodes if n.attr["is_page"]}
            #retrieve the attributes of interest from the relevant pages
            pages = Page.objects.filter(id__in=page_nodes.keys()).values('id','changed_by')
            for page in pages:
                #take the node referring to the page
                node =  page_nodes[page['id']]
                #put the changed_by attribute on the node
                node.attr['changed_by'] = page['changed_by']
        return nodes
menu_pool.register_modifier(PostModifier)
