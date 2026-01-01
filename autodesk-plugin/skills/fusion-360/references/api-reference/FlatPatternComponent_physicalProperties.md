# FlatPatternComponent.physicalProperties Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this component. Property values will be calculated using the 'LowCalculationAccuracy' setting when using this property to get the PhysicalProperties object. To specify a higher calculation tolerance, use the getPhysicalProperties method instead.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. Ptr<PhysicalProperties> propertyValue = flatPatternComponent_var->physicalProperties(); ``` ```` |

## Property Value

This is a read only property whose value is a [PhysicalProperties](PhysicalProperties.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |