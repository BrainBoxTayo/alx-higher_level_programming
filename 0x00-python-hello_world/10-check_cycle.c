#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it using floyd
 * algorithm
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slownode, *fastnode;

	if (list == NULL || list->next == NULL)
		return (0);

	slownode = list;
	fastnode = list->next;

	while (fastnode != NULL && fastnode->next != NULL)
	{
		if (slownode == fastnode)
			return (1);

		slownode = slownode->next;
		fastnode = fastnode->next->next;
	}

	return (0);
}

