#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: - Pointer to start of linked list
 *
 * Return: 0 if there is no cycle
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
