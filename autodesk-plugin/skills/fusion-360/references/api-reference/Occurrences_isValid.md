# Occurrences.isValid Property

Parent Object: [Occurrences](Occurrences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrences.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrences\_var" is a variable referencing an Occurrences object. |

"occurrences\_var" is a variable referencing an Occurrences object. ```` ``` #include <Fusion/Components/Occurrences.h>  // Get the value of the property. boolean propertyValue = occurrences_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |