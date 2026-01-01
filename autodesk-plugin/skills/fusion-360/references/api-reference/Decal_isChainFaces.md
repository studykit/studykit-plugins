# Decal.isChainFaces Property

Parent Object: [Decal](Decal.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decal.h>

## Description

Returns if the decal is limited to a specified set of faces or wraps onto all faces in the body. If this property is True, a single face has been specified and the decal can wrap onto other faces of the body. If False, the decal is limited to the set of specified faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decal\_var" is a variable referencing a Decal object.  ```` ``` # Get the value of the property. propertyValue = decal_var.isChainFaces ``` ```` |

"decal\_var" is a variable referencing a Decal object. ```` ``` #include <Fusion/Image/Decal.h>  // Get the value of the property. boolean propertyValue = decal_var->isChainFaces(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |