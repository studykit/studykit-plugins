# Setup.fixtures Property

Parent Object: [Setup](Setup.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

Gets and sets the fixtures associated with the setup, which are represented by an ObjectCollection of models, where a model can be an Occurrence, BRepBody, or MeshBody. To be able to set models as fixtures, the fixturesEnabled property has to be set first.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setup\_var" is a variable referencing a Setup object. |

"setup\_var" is a variable referencing a Setup object. ```` ``` #include <Cam/CAM/Setup.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = setup_var->fixtures();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = setup_var->fixtures(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |