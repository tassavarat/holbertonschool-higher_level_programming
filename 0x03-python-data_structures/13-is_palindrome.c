#include "lists.h"

/**
 * reverse_listint - Reverses a linked list
 * @head: Pointer to address of a list
 *
 * Return: Pointer to first node of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp, *cur, *rev;

	tmp = cur = *head;
	rev = NULL;
	while (cur)
	{
		tmp = tmp->next;
		cur->next = rev;
		rev = cur;
		cur = tmp;
	}
	return (rev);
}

/**
 * is_palindrome - Checks if singly linked list is palindrome
 * @head: Pointer to pointer of first node
 *
 * Return: 1 if palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *rev, *cur;

	fast = slow = cur = *head;
	if (*head)
	{
		while (fast && fast->next)
		{
			slow = slow->next;
			fast = fast->next->next;
		}
		rev = slow = reverse_listint(&slow);
		while (rev)
		{
			if (cur->n != rev->n)
				return (0);
			cur = cur->next;
			rev = rev->next;
		}
	reverse_listint(&slow);
	}
	return (1);
}
