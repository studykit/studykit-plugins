# FusionDocument.name Property

Parent Object: [FusionDocument](FusionDocument.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDocument.h>

## Description

This property gets and sets the name of the document. You can only set the name of a document before the document is saved for the first time. You can use the isSaved property to determine this. If the document has not been saved and the name is changed, the specified name will be the default name shown in the Save dialog, which the user can modify before saving the document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionDocument\_var" is a variable referencing a FusionDocument object.  ```` ``` # Get the value of the property. propertyValue = fusionDocument_var.name  # Set the value of the property. fusionDocument_var.name = propertyValue ``` ```` |

"fusionDocument\_var" is a variable referencing a FusionDocument object. ```` ``` #include <Fusion/Fusion/FusionDocument.h>  // Get the value of the property. string propertyValue = fusionDocument_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = fusionDocument_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |