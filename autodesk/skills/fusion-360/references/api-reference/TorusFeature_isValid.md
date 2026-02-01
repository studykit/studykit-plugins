# TorusFeature.isValid Property

Parent Object: [TorusFeature](TorusFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TorusFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torusFeature\_var" is a variable referencing a TorusFeature object. |

"torusFeature\_var" is a variable referencing a TorusFeature object. ```` ``` #include <Fusion/Features/TorusFeature.h>  // Get the value of the property. boolean propertyValue = torusFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |