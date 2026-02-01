# Occurrence.name Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

The name of the occurrence. This is the name as seen in the browser. It is a reflection of the component name with an added counter suffix (i.e. 'OccurrenceName:1').

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. string propertyValue = occurrence_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Assembly traversal using recursion API Sample](AssemblyTraversalUsingRecursion_Sample.htm) | Traverses the entire structure of the currently open assemlby using a recursive function and displays the result in a message box. This will match the occurrence structure seen in the browser. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |