# Leader Object

## Description

The Leader object represents a leader associated with a drawing annotation.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddLeader](../Leader/Leader_AddLeader.md) | Method that adds a leader branch with the input points. This is the equivalent of the 'Add Leader' command in the user interface. This method will succeed only if the HasRootNode property returns False (i.e. there are no existing leader segments). If there are existing leader segments, this method will fail you should use the LeaderNode.AddLeader method instead. |
| [GetReferenceKey](../Leader/Leader_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllLeafNodes](../Leader/Leader_AllLeafNodes.md) | Property that returns a flat collection of all the leaf nodes in the leader tree. This property will return Nothing if the HasRootNode property returns False. |
| [AllNodes](../Leader/Leader_AllNodes.md) | Property that returns a flat collection of all the nodes in the leader tree. This property will return Nothing if the HasRootNode property returns False. |
| [Application](../Leader/Leader_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowheadType](../Leader/Leader_ArrowheadType.md) | Gets and sets the arrowhead type of the leader. |
| [AttributeSets](../Leader/Leader_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [HasRootNode](../Leader/Leader_HasRootNode.md) | Property that returns if a root node exists for this leader. If False, there are no leader segments associated with this leader and the RootNode property will return Nothing. |
| [Parent](../Leader/Leader_Parent.md) | Property that returns the parent of this leader object. |
| [RootNode](../Leader/Leader_RootNode.md) | Property that returns the root node of this leader. This property will return Nothing if the HasRootNode property returns False. |
| [Type](../Leader/Leader_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Balloon.Leader](../Balloon/Balloon_Leader.md), [BendNote.Leader](../BendNote/BendNote_Leader.md), [ChamferNote.Leader](../ChamferNote/ChamferNote_Leader.md), [DrawingWeldingSymbol.Leader](../DrawingWeldingSymbol/DrawingWeldingSymbol_Leader.md), [FeatureControlFrame.Leader](../FeatureControlFrame/FeatureControlFrame_Leader.md), [HoleTag.Leader](../HoleTag/HoleTag_Leader.md), [LeaderNote.Leader](../LeaderNote/LeaderNote_Leader.md), [PunchNote.Leader](../PunchNote/PunchNote_Leader.md), [SketchedSymbol.Leader](../SketchedSymbol/SketchedSymbol_Leader.md), [SurfaceTextureSymbol.Leader](../SurfaceTextureSymbol/SurfaceTextureSymbol_Leader.md), [TransitionSymbol.Leader](../TransitionSymbol/TransitionSymbol_Leader.md)

## Version

Introduced in version 11
