#include "lists.h"
/**
 * listint_len - returns the number of elements in a list
 * @h: head
 * Return: number of elements
 */
int listint_len(const listint_t *h)
{
	size_t count = 0;
	const listint_t *node = h;

	while (node != NULL)
	{
		node = node->next;
		count++;
	}
	return (count);
}
/**
 * mirror_arr - mirrors the array of n's
 * @arr: array of n's of the list
 * @n: size of the array
 * Return: pointer to new array of n's
 */
int *mirror_arr(int *arr, int n)
{
	int i, j = 0;
	int *new_arr = malloc(n * sizeof(int));

	for (i = 0; i < n; i++)
	{
		new_arr[i] = arr[i];
	}
	for (i = 0; i < (n / 2); i++)
	{
		j = new_arr[i];
		new_arr[i] = new_arr[n - i - 1];
		new_arr[n - i - 1] = j;
	}
	return (new_arr);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to a linked list
 * Return: 0 if not a palindrome 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current = NULL;
	listint_t *present = *head;
	int n, i = 0, j = 0;
	/*arr holds the n values of each node*/
	int *arr, *new_arr, value;

	if (*head == NULL)
		return (1);
	current = *head;
	n = listint_len(current);
	arr = malloc(n * sizeof(int));
	if (arr == NULL)
		return (10);
	present = *head;
	while (present != NULL)
	{
		arr[i] = present->n;
		present = present->next;
		i++;
	}
	new_arr = mirror_arr(arr, n);
	while (arr[j] == new_arr[j])
	{
		j++;
		if (j == n)
		{
			value = 1;
			free(arr), free(new_arr);
			return (value);
		}
	}
	value = 0;
	free(arr), free(new_arr);
	return (value);
}
