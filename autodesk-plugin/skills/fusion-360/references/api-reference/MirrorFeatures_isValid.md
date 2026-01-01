# MirrorFeatures.isValid Property

Parent Object: [MirrorFeatures](MirrorFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeatures\_var" is a variable referencing a MirrorFeatures object. |

"mirrorFeatures\_var" is a variable referencing a MirrorFeatures object. ```` ``` #include <Fusion/Features/MirrorFeatures.h>  // Get the value of the property. boolean propertyValue = mirrorFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |