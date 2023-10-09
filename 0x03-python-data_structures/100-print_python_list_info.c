#include <Python.h>

/**
 * print_python_list_info - prints basic info about Pyrhon Lists
 * @p: PyObject List
 */

void print_python_list_info(PyObject *p)
{
	int size, allocate, i;
	PyObject *obj;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (i = 0; i < size; i++)
	{
		printf("Element %d:", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);

	}
}
