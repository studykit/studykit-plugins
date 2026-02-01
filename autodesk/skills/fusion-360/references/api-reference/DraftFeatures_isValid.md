# DraftFeatures.isValid Property

Parent Object: [DraftFeatures](DraftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatures\_var" is a variable referencing a DraftFeatures object. |

"draftFeatures\_var" is a variable referencing a DraftFeatures object. ```` ``` #include <Fusion/Features/DraftFeatures.h>  // Get the value of the property. boolean propertyValue = draftFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |