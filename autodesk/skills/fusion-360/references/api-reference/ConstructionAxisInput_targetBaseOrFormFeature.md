# ConstructionAxisInput.targetBaseOrFormFeature Property

Parent Object: [ConstructionAxisInput](ConstructionAxisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisInput.h>

## Description

When creating a construction axis that is owned by a base or form feature, set this property to the base or form feature you want to associate the new construction plane with. By default, this is null, meaning it will not be associated with a base or form feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisInput\_var" is a variable referencing a ConstructionAxisInput object.  ```` ``` # Get the value of the property. propertyValue = constructionAxisInput_var.targetBaseOrFormFeature  # Set the value of the property. constructionAxisInput_var.targetBaseOrFormFeature = propertyValue ``` ```` |

"constructionAxisInput\_var" is a variable referencing a ConstructionAxisInput object. ```` ``` #include <Fusion/Construction/ConstructionAxisInput.h>  // Get the value of the property. Ptr<Base> propertyValue = constructionAxisInput_var->targetBaseOrFormFeature();  // Set the value of the property, where value_var is a Base. bool returnValue = constructionAxisInput_var->targetBaseOrFormFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |