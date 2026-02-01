# ConstructionPointInput.targetBaseOrFormFeature Property

Parent Object: [ConstructionPointInput](ConstructionPointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointInput.h>

## Description

When creating a construction point that is owned by a base or form feature, set this property to the base or form feature you want to associate the new construction point with. By default, this is null, meaning it will not be associated with a base or form feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointInput\_var" is a variable referencing a ConstructionPointInput object.  ```` ``` # Get the value of the property. propertyValue = constructionPointInput_var.targetBaseOrFormFeature  # Set the value of the property. constructionPointInput_var.targetBaseOrFormFeature = propertyValue ``` ```` |

"constructionPointInput\_var" is a variable referencing a ConstructionPointInput object. ```` ``` #include <Fusion/Construction/ConstructionPointInput.h>  // Get the value of the property. Ptr<Base> propertyValue = constructionPointInput_var->targetBaseOrFormFeature();  // Set the value of the property, where value_var is a Base. bool returnValue = constructionPointInput_var->targetBaseOrFormFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |