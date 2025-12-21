# CircularOccurrencePatternProxy Object

Derived from: [CircularOccurrencePattern](../CircularOccurrencePattern/CircularOccurrencePattern.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Delete.md) | Method that deletes the pattern. |
| [GetReferenceKey](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Suppress](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Suppress.md) | Suppress the occurrence pattern. |
| [Unsuppress](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Unsuppress.md) | Unsuppress the occurrence pattern. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AngleOffset](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_AngleOffset.md) | Property returning the Parameter object that controls the angle offset between pattern instances. |
| [Application](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AxisEntity](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_AxisEntity.md) | Gets/Sets the entity used to define the axis of the pattern. |
| [AxisEntityNaturalDirection](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_AxisEntityNaturalDirection.md) | Gets/Sets whether the axis direction is in the natural direction of the axis entity or not. |
| [ContainingOccurrence](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ElementCount](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_ElementCount.md) | Property returning the Parameter object that controls the number of elements in the pattern. |
| [HealthStatus](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsPatternElement](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_IsPatternElement.md) | Property that indicates whether this occurrence pattern is itself an element of a parent pattern. In the case where this occurrence pattern represents a pattern element, this property returns True. The PatternElement property can be used to get that pattern element. |
| [LockRotation](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_LockRotation.md) | Read-write property that gets and sets whether the patterned elements keep the same rotation as their parent occurrences. This defaults to False when the CircularOccurrencePattern is just created indicates that the patterned elements will be rotated. |
| [Name](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Name.md) | Gets/Sets the name for the pattern. |
| [NativeObject](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OccurrencePatternElements](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_OccurrencePatternElements.md) | Property returning an OccurrencePatternElements collection object. The first element within this collection will contain the components that were provided as input for the pattern. |
| [Parent](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Parent.md) | Property that returns the parent of the object. |
| [ParentComponents](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_ParentComponents.md) | Property that gets and sets the components used as input for the pattern. |
| [PatternElement](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_PatternElement.md) | Property that returns the pattern element this occurrence pattern represents. In the case where this occurrence pattern is not part of a parent pattern this property returns Nothing. The IsPatternElement property can be used to check if this occurrence pattern is part of a parent pattern. |
| [PatternRadiusPoint](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_PatternRadiusPoint.md) | Read-write property that gets and sets the point used to define the pattern radius against the rotation axis. This property returns Nothing when the LockRotation is False. When the LockRotation is set to True, this property returns a Point object indicating th. |
| [PositioningMethod](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_PositioningMethod.md) | Read-write property that gets and sets the enum indicating the positioning method used for the component pattern. |
| [Suppressed](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Suppressed.md) | Returns the suppress state of the occurrence pattern. |
| [Type](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Visible.md) | Gets/Sets the Visible property for the pattern. |

## Version

Introduced in version 2010
