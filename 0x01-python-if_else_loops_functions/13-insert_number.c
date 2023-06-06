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
	current = *head;
	while (current->next != NULL)
	{
		if (current->n < number && current->next->n < number)
		{
			current = current->next;
			ctr++;
		}
		else if (current->n < number && current->next->n > number)
		{
			new->next = current->next;
			current->next = new;
			break;
		}
	}
	return (new);
}
