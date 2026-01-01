# OccurrenceList.isValid Property

Parent Object: [OccurrenceList](OccurrenceList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/OccurrenceList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrenceList\_var" is a variable referencing an OccurrenceList object. |

"occurrenceList\_var" is a variable referencing an OccurrenceList object. ```` ``` #include <Fusion/Components/OccurrenceList.h>  // Get the value of the property. boolean propertyValue = occurrenceList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |