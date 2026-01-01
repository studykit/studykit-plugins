# DraftFeature.plane Property

Parent Object: [DraftFeature](DraftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeature.h>

## Description

Gets and sets the plane that defines the direction in which the draft is applied. This can be a planar BrepFace, or a ConstructionPlane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeature\_var" is a variable referencing a DraftFeature object.  ```` ``` # Get the value of the property. propertyValue = draftFeature_var.plane  # Set the value of the property. draftFeature_var.plane = propertyValue ``` ```` |

"draftFeature\_var" is a variable referencing a DraftFeature object. ```` ``` #include <Fusion/Features/DraftFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = draftFeature_var->plane();  // Set the value of the property, where value_var is a Base. bool returnValue = draftFeature_var->plane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |