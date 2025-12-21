# OccurrencePatternElementProxy Object

Derived from: [OccurrencePatternElement](../OccurrencePatternElement/OccurrencePatternElement.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Components](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_Components.md) | Property that returns the set of components that were created for this particular instance. There are cases where this collection can contain a count of zero. The obvious cases are when this element has been set to be independent or suppressed. There is another case when this element is the result of a feature based occurrence pattern and the instance it is associated with within the feature pattern has been suppressed. |
| [ContainingOccurrence](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Independent](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_Independent.md) | Gets/Sets whether the element is independent of the pattern or not. |
| [Index](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_Index.md) | Property that returns the index of this element within the OccurrencePatternElements collection it is a member of. |
| [Name](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_Name.md) | Property that returns the name of the element. |
| [NativeObject](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Occurrences](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_Occurrences.md) | Property that returns the set of occurrences that were created for this particular instance. |
| [Parent](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_Parent.md) | Property that returns the parent occurrence pattern of the object. |
| [Suppressed](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_Suppressed.md) | Gets/Sets whether the element is suppressed or not. |
| [Type](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2010
