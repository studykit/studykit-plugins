# DraftFeatureInput.plane Property

Parent Object: [DraftFeatureInput](DraftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatureInput.h>

## Description

Gets and sets the plane that defines the direction in which the draft is applied. This can be a planar BrepFace, or a ConstructionPlane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object. |

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object. ```` ``` #include <Fusion/Features/DraftFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = draftFeatureInput_var->plane();  // Set the value of the property, where value_var is a Base. bool returnValue = draftFeatureInput_var->plane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |