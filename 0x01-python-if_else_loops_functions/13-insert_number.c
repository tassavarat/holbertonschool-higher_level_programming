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

	if (number < tmp->n)
		addstart = 1;
	while (tmp->next && number > tmp->next->n && !addstart)
	{
		if (!tmp)
			return (NULL);
		tmp = tmp->next;
	}
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
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
