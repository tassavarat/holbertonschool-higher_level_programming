#include "lists.h"

/**
 * insert_node - Inserts number into singly sorted list
 * @head: Pointer to start of linked list
 * @number: Number to initialise node member
 *
 * Return: Address of new node
 * NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new;
	int addstart;

	tmp = *head;
	addstart = 0;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	if (!tmp && !head)
		return (NULL);
	else if (!*head)
	{
		*head = new;
		new->n = number;
		new->next = NULL;
		return (new);
	}
	else if (number < tmp->n)
		addstart = 1;
	while (tmp->next && number > tmp->next->n && !addstart)
		tmp = tmp->next;
	if (!addstart)
	{
		new->next = tmp->next;
		tmp->next = new;
	}
	else
	{
		new->next = tmp;
		*head = new;
	}
	new->n = number;
	return (new);
}
