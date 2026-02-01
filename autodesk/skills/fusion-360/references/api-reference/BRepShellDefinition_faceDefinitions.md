# BRepShellDefinition.faceDefinitions Property

Parent Object: [BRepShellDefinition](BRepShellDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShellDefinition.h>

## Description

Provides access to the BRepFaceDefinitions object associated with this BRepShellDefinition. It's through the returned collection that you can create new BRepFaceDefinition objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShellDefinition\_var" is a variable referencing a BRepShellDefinition object. |

"bRepShellDefinition\_var" is a variable referencing a BRepShellDefinition object. ```` ``` #include <Fusion/BRep/BRepShellDefinition.h>  // Get the value of the property. Ptr<BRepFaceDefinitions> propertyValue = bRepShellDefinition_var->faceDefinitions(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaceDefinitions](BRepFaceDefinitions.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body definition Sample](BRepBodyDefinition_Sample.htm) | Demonstrates creating BRep bodies by BRepBodyDefinition. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |