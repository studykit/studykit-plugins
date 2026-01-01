# LoftSections.add Method

Parent Object: [LoftSections](LoftSections.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSections.h>

## Description

Adds a new section to the loft. The initial end condition is "Free". Additional methods on the returned LoftSection can be used to further define the section.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSections\_var" is a variable referencing a [LoftSections](LoftSections.htm) object.```` ``` returnValue = loftSections_var.add(entity) ``` ```` |

"loftSections\_var" is a variable referencing a [LoftSections](LoftSections.htm) object.  ```` ``` #include <Fusion/Features/LoftSections.h>  returnValue = loftSections_var->add(entity); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LoftSection](LoftSection.htm) | Returns the newly created LoftSection object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entity | [Base](Base.htm) | Specifies the BRepFace, Profile, Path, SketchPoint, ConstructionPoint, or an ObjectCollection containing a contiguous set of Profile objects that defines the section. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [loftFeatures.add](loftFeatures_add_Sample.htm) | Demonstrates the loftFeatures.add method. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |