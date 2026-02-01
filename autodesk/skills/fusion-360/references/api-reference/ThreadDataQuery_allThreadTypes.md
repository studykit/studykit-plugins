# ThreadDataQuery.allThreadTypes Property

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

This method returns an array of all the available thread types (families). The type names are always English. This English name should be used in the other methods that take the type as an input argument. If you need to display the type name to the user, you can use the threadTypeCustomName method To get the localized name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadDataQuery\_var" is a variable referencing a ThreadDataQuery object. |

"threadDataQuery\_var" is a variable referencing a ThreadDataQuery object. ```` ``` #include <Fusion/Features/ThreadDataQuery.h>  // Get the value of the property. std::vector<string> propertyValue = threadDataQuery_var->allThreadTypes(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature API Sample](ThreadFeatureSample_Sample.htm) | Demonstrates creating a new thread feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |