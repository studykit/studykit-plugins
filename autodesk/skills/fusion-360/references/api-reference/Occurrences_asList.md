# Occurrences.asList Property

Parent Object: [Occurrences](Occurrences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrences.h>

## Description

Returns the contents of this collection as an OccurrencesList object. This is useful when writing a function that traverses an assembly.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrences\_var" is a variable referencing an Occurrences object. |

"occurrences\_var" is a variable referencing an Occurrences object. ```` ``` #include <Fusion/Components/Occurrences.h>  // Get the value of the property. Ptr<OccurrenceList> propertyValue = occurrences_var->asList(); ``` ```` |

## Property Value

This is a read only property whose value is an [OccurrenceList](OccurrenceList.htm).

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