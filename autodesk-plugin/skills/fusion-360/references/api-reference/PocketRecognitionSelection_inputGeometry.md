# PocketRecognitionSelection.inputGeometry Property

Parent Object: [PocketRecognitionSelection](PocketRecognitionSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketRecognitionSelection.h>

## Description

Get or set the value of the input geometry. If the value originates from a component instead of an occurrence, or an occurrence outside of the CAM environment, then the subpath is checked against the CAM model tree. For some child classes, this may be the same as the value property, but might also consist of fewer elements. Valid elements depend on the capabilities of the derived class. An exception is thrown if the matching fails or the given entity does not match the expected type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object. |

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object. ```` ``` #include <Cam/GeometrySelections/PocketRecognitionSelection.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = pocketRecognitionSelection_var->inputGeometry();  // Set the value of the property, where value_var is a Base. bool returnValue = pocketRecognitionSelection_var->inputGeometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |