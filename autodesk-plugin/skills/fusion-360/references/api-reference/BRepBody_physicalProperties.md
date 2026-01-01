# BRepBody.physicalProperties Property

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this body. Property values will be calculated using the 'LowCalculationAccuracy' setting when using this property to get the PhysicalProperties object. To specify a higher calculation tolerance, use the getPhysicalProperties method on the Design class instead.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a BRepBody object. |

"bRepBody\_var" is a variable referencing a BRepBody object. ```` ``` #include <Fusion/BRep/BRepBody.h>  // Get the value of the property. Ptr<PhysicalProperties> propertyValue = bRepBody_var->physicalProperties(); ``` ```` |

## Property Value

This is a read only property whose value is a [PhysicalProperties](PhysicalProperties.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Physical Properties API Sample](GetPhysicalProperties_Sample.htm) | Script that demonstrates getting physical properties using the API. When this script is run it will create a new document, build a simple model, and get the various physical properties from the model. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |