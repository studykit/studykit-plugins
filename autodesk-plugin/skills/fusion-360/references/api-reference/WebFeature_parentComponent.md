# WebFeature.parentComponent Property

Parent Object: [WebFeature](WebFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/WebFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webFeature\_var" is a variable referencing a WebFeature object. |

"webFeature\_var" is a variable referencing a WebFeature object. ```` ``` #include <Fusion/Features/WebFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = webFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |