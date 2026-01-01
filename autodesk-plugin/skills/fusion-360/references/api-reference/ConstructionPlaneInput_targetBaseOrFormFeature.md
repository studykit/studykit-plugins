# ConstructionPlaneInput.targetBaseOrFormFeature Property

Parent Object: [ConstructionPlaneInput](ConstructionPlaneInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneInput.h>

## Description

When creating a construction plane that is owned by a base or form feature, set this property to the base or form feature you want to associate the new construction plane with. By default, this is null, meaning it will not be associated with a base or form feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneInput\_var" is a variable referencing a ConstructionPlaneInput object.  ```` ``` # Get the value of the property. propertyValue = constructionPlaneInput_var.targetBaseOrFormFeature  # Set the value of the property. constructionPlaneInput_var.targetBaseOrFormFeature = propertyValue ``` ```` |

"constructionPlaneInput\_var" is a variable referencing a ConstructionPlaneInput object. ```` ``` #include <Fusion/Construction/ConstructionPlaneInput.h>  // Get the value of the property. Ptr<Base> propertyValue = constructionPlaneInput_var->targetBaseOrFormFeature();  // Set the value of the property, where value_var is a Base. bool returnValue = constructionPlaneInput_var->targetBaseOrFormFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BaseFeature Sample](BaseFeatureSample_Sample.htm) | Creates a new base feature. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |