#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *          Otherwise - 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list->next;
	hare = (list->next)->next;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = (hare->next)->next;

		if (tortoise == hare)
			return (1);
	}

	return (0);
}
