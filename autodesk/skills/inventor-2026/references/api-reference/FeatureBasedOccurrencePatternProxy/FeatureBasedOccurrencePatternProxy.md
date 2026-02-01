# FeatureBasedOccurrencePatternProxy Object

Derived from: [FeatureBasedOccurrencePattern](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Delete.md) | Method that deletes the pattern. |
| [GetReferenceKey](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Suppress](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Suppress.md) | Suppress the occurrence pattern. |
| [Unsuppress](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Unsuppress.md) | Unsuppress the occurrence pattern. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [FeaturePattern](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_FeaturePattern.md) | Gets/Sets the feature pattern used as input for this occurrence pattern. |
| [HealthStatus](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsPatternElement](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_IsPatternElement.md) | Property that indicates whether this occurrence pattern is itself an element of a parent pattern. In the case where this occurrence pattern represents a pattern element, this property returns True. The PatternElement property can be used to get that pattern element. |
| [Name](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Name.md) | Gets/Sets the name for the pattern. |
| [NativeObject](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OccurrencePatternElements](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_OccurrencePatternElements.md) | Property returning an OccurrencePatternElements collection object. The first element within this collection will contain the components that were provided as input for the pattern. |
| [Parent](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Parent.md) | Property that returns the parent of the object. |
| [ParentComponents](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_ParentComponents.md) | Property that gets and sets the components used as input for the pattern. |
| [PatternElement](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_PatternElement.md) | Property that returns the pattern element this occurrence pattern represents. In the case where this occurrence pattern is not part of a parent pattern this property returns Nothing. The IsPatternElement property can be used to check if this occurrence pattern is part of a parent pattern. |
| [Suppressed](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Suppressed.md) | Returns the suppress state of the occurrence pattern. |
| [Type](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Visible.md) | Gets/Sets the Visible property for the pattern. |

## Version

Introduced in version 2010
