# SetupInput.stockSolids Property

Parent Object: [SetupInput](SetupInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupInput.h>

## Description

An array of models, where a model can be an Occurrence, ManufacturingModel, BRepBody, or MeshBody. Setting this property, or adding the first object to the returned array will automatically set the stockMode to "SolidStock".

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupInput\_var" is a variable referencing a SetupInput object.  ```` ``` # Get the value of the property. propertyValue = setupInput_var.stockSolids  # Set the value of the property. setupInput_var.stockSolids = propertyValue ``` ```` |

"setupInput\_var" is a variable referencing a SetupInput object. ```` ``` #include <Cam/CAM/SetupInput.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = setupInput_var->stockSolids();  // Set the value of the property, where value_var is a Base. bool returnValue = setupInput_var->stockSolids(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |