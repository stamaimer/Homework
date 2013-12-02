#ifndef GRAMMER_TREE_NODE_H
#define GRAMMER_TREE_NODE_H

#include <list>

class GrammerTreeNode
{
public:
	GrammerTreeNode(arguments);
	~GrammerTreeNode();

private:
	list<GrammerTreeNode> childrens_;
	GrammerTreeNodeType type_;
};

#endif // GRAMMER_TREE_NODE_H 

		