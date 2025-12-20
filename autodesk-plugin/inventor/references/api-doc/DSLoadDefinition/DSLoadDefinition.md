# DSLoadDefinition Object

## Description

DSLoadDefinition Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../DSLoadDefinition/DSLoadDefinition_Copy.md) | Creates a copy of this DSLoadDefinition object. The new DSLoadDefinition object is independent of any load. It can edited and used as input to edit an existing load or to create a new load. Creating a copy of a definition, editing it, and then assigning it back to the load can be a more efficient way of editing multiple inputs because it results in a single recompute. |
| [SetByMagnitudeAndDirection](../DSLoadDefinition/DSLoadDefinition_SetByMagnitudeAndDirection.md) | Specifies the direction and magnitude of this load to be defined by a magnitude value and a direction defined by an entity. |
| [SetByVector](../DSLoadDefinition/DSLoadDefinition_SetByVector.md) | Specifies the direction and magnitude of this load to be defined by the x, y, z components of a vector. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DSLoadDefinition/DSLoadDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DirectionEntity](../DSLoadDefinition/DSLoadDefinition_DirectionEntity.md) | Gets and sets Entity that defines the direction of the load. Valid geometry includes planar and cylindrical faces, and linear edges. |
| [GlyphColor](../DSLoadDefinition/DSLoadDefinition_GlyphColor.md) | Gets and sets the color of the force or torque glyph as seen during the playback of the simulation. The IsDisplayed property controls whether the glyph is displayed or not. |
| [GlyphScale](../DSLoadDefinition/DSLoadDefinition_GlyphScale.md) | Gets and sets the scale of the load glyph. This property is writable when the DSLoadDefinition object has been created using the DSLoads.CreateLoadDefinition or DSLoadDefinition.Copy methods. |
| [IsAssociativeLoadDirection](../DSLoadDefinition/DSLoadDefinition_IsAssociativeLoadDirection.md) | Gets and sets the how the direction of the force or torque is defined. If True, the direction of the force or torque is defined relative to the coordinate system of the component containing the force or torque. If False, the direction of the force or torque. |
| [IsDefinedByVectorComponents](../DSLoadDefinition/DSLoadDefinition_IsDefinedByVectorComponents.md) | Gets and sets if the magnitude and direction of this load is defined by vector components or a specified magnitude and direction entity. |
| [IsDirectionEntityNaturalDirection](../DSLoadDefinition/DSLoadDefinition_IsDirectionEntityNaturalDirection.md) | Gets and sets whether the direction of the load, when defined by an entity, is in the natural direction defined by the entity or reversed. |
| [IsDisplayed](../DSLoadDefinition/DSLoadDefinition_IsDisplayed.md) | Gets and sets if the arrow for the force or torque is displayed during the playback of the simulation. |
| [IsSuppressed](../DSLoadDefinition/DSLoadDefinition_IsSuppressed.md) | Gets and sets whether the load is suppressed. |
| [Location](../DSLoadDefinition/DSLoadDefinition_Location.md) | Gets the location of the load. The location is defined by specifying geometry and the location coordinate is inferred from the selected geometry. This provides that inferred coordinate regardless of the entity that was used to specify the location. |
| [LocationEntity](../DSLoadDefinition/DSLoadDefinition_LocationEntity.md) | Gets and sets Entity that defines the location of the load. |
| [Magnitude](../DSLoadDefinition/DSLoadDefinition_Magnitude.md) | Gets the DSValue object that defines the magnitude of the load. The value of the magnitude can be accessed through the returned DSValue object.  This property returns Nothing in the case where the IsDefinedByVectorComponents is True. To change the definition of the load to be defined by a magnitude and direction use the SetByMagnitudeAndDirection method.  Setting the magnitude using the SetValueUsingArray method of the DSValue object is currently limited to motion, magnitude, and x,y,z coordinates. |
| [Parent](../DSLoadDefinition/DSLoadDefinition_Parent.md) | Gets the parent DSLoad object this definition object is associated with. If this definition is not associated with a load then this property returns Nothing. |
| [Type](../DSLoadDefinition/DSLoadDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Vector](../DSLoadDefinition/DSLoadDefinition_Vector.md) | Gets a Vector indicating the vector of the load. This can be used to get the load vector regardless of whether it has been defined using geometry or the x, y, z, components. |
| [VectorXComponent](../DSLoadDefinition/DSLoadDefinition_VectorXComponent.md) | Gets the DSValue object that defines the X component of the vector. This property returns Nothing in the case where the IsDefinedByVectorComponents is False. To change the definition of the load to be defined by a vector use the SetByVector method. |
| [VectorYComponent](../DSLoadDefinition/DSLoadDefinition_VectorYComponent.md) | Gets the DSValue object that defines the Y component of the vector. This property returns Nothing in the case where the IsDefinedByVectorComponents is False. To change the definition of the load to be defined by a vector use the SetByVector method. |
| [VectorZComponent](../DSLoadDefinition/DSLoadDefinition_VectorZComponent.md) | Gets the DSValue object that defines the Z component of the vector. This property returns Nothing in the case where the IsDefinedByVectorComponents is False. To change the definition of the load to be defined by a vector use the SetByVector method. |

## Accessed From

[DSLoad.Definition](../DSLoad/DSLoad_Definition.md), [DSLoadDefinition.Copy](../DSLoadDefinition/DSLoadDefinition_Copy.md)

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |