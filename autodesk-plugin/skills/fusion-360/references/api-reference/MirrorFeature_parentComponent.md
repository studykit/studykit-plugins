# MirrorFeature.parentComponent Property

Parent Object: [MirrorFeature](MirrorFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. |

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. ```` ``` #include <Fusion/Features/MirrorFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = mirrorFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |