#include "lists.h"
/**
 * insert_node - inserts a node in a sorted list
 * @head: pointer to pointer of first node
 * @number: new number to be inserted
 * Return: new node adress
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;
	size_t ctr = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;
	if (current == NULL)
	{
		*head = new;
		return (new);
	}
	while (current != NULL)
	{
		if (current->next == NULL)
		{
			new->next = NULL;
			current->next = new;
			return (new);
		}
		if (number < current->n  && number < current->next->n)
		{
			new->next = current;
			*head = new;
			return (new);
		}
		else if (current->n < number && current->next->n >= number)
		{
			new->next = current->next;
			current->next = new;
			break;
		}
		current = current->next;
		ctr++;
	}
	return (new);
}
