# SectionAnalyses.createInput Method

Parent Object: [SectionAnalyses](SectionAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalyses.h>

## Description

Creates a new SectionAnalysisInput object to use when creating a new Section Analysis. A SectionAnalysisInput object is the API equivalent of the command dialog that contains the inputs to create a section analysis. Use this object to define the settings you need and then pass this into the add method to create the section analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalyses\_var" is a variable referencing a [SectionAnalyses](SectionAnalyses.htm) object.```` ``` returnValue = sectionAnalyses_var.createInput(cutPlaneEntity, distance) ``` ```` |

"sectionAnalyses\_var" is a variable referencing a [SectionAnalyses](SectionAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SectionAnalysisInput](SectionAnalysisInput.htm) | Returns a SectionAnalysisInput object if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| cutPlaneEntity | [Base](Base.htm) | The planar entity used to define the cut plane and can be either a planar BRepFace or a ConstructionPlane object. |
| distance | double | The offset distance of the section from the cut plane. A positive value will offset in the positive normal direction of the cut plane entity. The value is in centimeters. This value is used to create a transformation matrix that defines the specified offset. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |