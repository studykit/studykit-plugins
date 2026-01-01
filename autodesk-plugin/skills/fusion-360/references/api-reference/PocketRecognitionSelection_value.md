# PocketRecognitionSelection.value Property

Parent Object: [PocketRecognitionSelection](PocketRecognitionSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketRecognitionSelection.h>

## Description

Returns the resulting value of the selection. In general, this returns the input selection, but child classes can override the return value if needed. Refer to the child classes comments for further details. The collection may contain duplicates. For OperationInputs, the return value may not be the same as for Operations, as additional geometry selected by child classes is not evaluated for OperationInputs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object. |

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object. ```` ``` #include <Cam/GeometrySelections/PocketRecognitionSelection.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = pocketRecognitionSelection_var->value(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |