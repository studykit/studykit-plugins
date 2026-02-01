# TorusFeature.parentComponent Property

Parent Object: [TorusFeature](TorusFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TorusFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torusFeature\_var" is a variable referencing a TorusFeature object. |

"torusFeature\_var" is a variable referencing a TorusFeature object. ```` ``` #include <Fusion/Features/TorusFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = torusFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |