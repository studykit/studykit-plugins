# MirrorFeatures.createInput Method

Parent Object: [MirrorFeatures](MirrorFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatures.h>

## Description

Creates a MirrorFeatureInput object. Use properties and methods on this object to define the mirror you want to create and then use the Add method, passing in the MirrorFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeatures\_var" is a variable referencing a [MirrorFeatures](MirrorFeatures.htm) object.```` ``` returnValue = mirrorFeatures_var.createInput(inputEntities, mirrorPlane) ``` ```` |

"mirrorFeatures\_var" is a variable referencing a [MirrorFeatures](MirrorFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MirrorFeatureInput](MirrorFeatureInput.htm) | Returns the newly created MirrorFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEntities | [ObjectCollection](ObjectCollection.htm) | A collection of the entities to mirror. It can contain faces, features, bodies, or components. The input must all be of a single type. For example, you can't provide a body and a component but the collection must be either all bodies or all components. |
| mirrorPlane | [Base](Base.htm) | Input planar entity that defines the mirror plane. This can be either a planar face or a construction plane. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [mirrorFeatures.add](mirrorFeatures_add_Sample.htm) | Demonstrates the mirrorFeatures.add method by mirroring the selected body around the base X-Y construction plane. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |