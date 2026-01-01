# Occurrence.documentReference Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

When the component this occurrence references is an external reference (the isReferencedComponent property returns true), this will return the object that represents that reference. Through the DocumentReference object you can modify the version and get other information associated with the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object.  ```` ``` # Get the value of the property. propertyValue = occurrence_var.documentReference ``` ```` |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<DocumentReference> propertyValue = occurrence_var->documentReference(); ``` ```` |

## Property Value

This is a read only property whose value is a [DocumentReference](DocumentReference.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |