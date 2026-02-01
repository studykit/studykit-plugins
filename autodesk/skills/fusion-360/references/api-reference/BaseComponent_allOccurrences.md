# BaseComponent.allOccurrences Property

Parent Object: [BaseComponent](BaseComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BaseComponent.h>

## Description

Returns all of the occurrences in the assembly regardless of their level within the assembly structure. The returned list is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseComponent\_var" is a variable referencing a BaseComponent object. |

"baseComponent\_var" is a variable referencing a BaseComponent object. ```` ``` #include <Fusion/Components/BaseComponent.h>  // Get the value of the property. Ptr<OccurrenceList> propertyValue = baseComponent_var->allOccurrences(); ``` ```` |

## Property Value

This is a read only property whose value is an [OccurrenceList](OccurrenceList.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |