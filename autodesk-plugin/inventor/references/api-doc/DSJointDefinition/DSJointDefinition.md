# DSJointDefinition Object

## Description

DSJointDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../DSJointDefinition/DSJointDefinition_Copy.md) | Creates a copy of this DSJointDefinition object. The new DSJointDefinition object is independent of any joint. It can edited and used as input to edit an existing joint or to create a new joint. Creating a copy of a definition, editing it, and then assigning it back to the joint can be a more efficient way of editing multiple inputs because it results in a single recompute. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DSJointDefinition/DSJointDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DegreesOfFreedom](../DSJointDefinition/DSJointDefinition_DegreesOfFreedom.md) | Gets the DSDegreesOfFreedom collection object provides access to the degrees of freedom associated with this joint. |
| [ForceGlyphColor](../DSJointDefinition/DSJointDefinition_ForceGlyphColor.md) | Gets and sets the color of the force glyph as seen during the playback of the simulation. |
| [ForceGlyphScale](../DSJointDefinition/DSJointDefinition_ForceGlyphScale.md) | Gets and sets the scale of the force glyph. |
| [IsDOFsLocked](../DSJointDefinition/DSJointDefinition_IsDOFsLocked.md) | Gets and sets whether the degrees of freedom are locked. |
| [IsForceDisplayed](../DSJointDefinition/DSJointDefinition_IsForceDisplayed.md) | Gets and sets whether the force glyph is displayd. |
| [IsLoadDisplayed](../DSJointDefinition/DSJointDefinition_IsLoadDisplayed.md) | Gets and sets whether the load glyph is displayed. |
| [IsSuppressed](../DSJointDefinition/DSJointDefinition_IsSuppressed.md) | Gets and sets whether the joint is suppressed. |
| [LoadGlyphColor](../DSJointDefinition/DSJointDefinition_LoadGlyphColor.md) | Gets and sets the color of the load glyph as seen during the playback of the simulation. |
| [LoadGlyphScale](../DSJointDefinition/DSJointDefinition_LoadGlyphScale.md) | Gets and sets the scale of the load glyph. |
| [Parent](../DSJointDefinition/DSJointDefinition_Parent.md) | Gets the parent DSJoint object this definition is associated with. This can return Nothing in the case where the definition is not associated with any joint. |
| [Type](../DSJointDefinition/DSJointDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DSDegreeOfFreedom.Parent](../DSDegreeOfFreedom/DSDegreeOfFreedom_Parent.md), [DSJoint.Definition](../DSJoint/DSJoint_Definition.md), [DSJointDefinition.Copy](../DSJointDefinition/DSJointDefinition_Copy.md)

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |