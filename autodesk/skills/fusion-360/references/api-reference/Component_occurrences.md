# Component.occurrences Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Property that returns the Occurrences collection associated with this component. This provides access to the occurrences at the top-level of this component and provides the functionality to add new occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<Occurrences> propertyValue = component_var->occurrences(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrences](Occurrences.htm).

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