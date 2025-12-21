# PresentationSnapshotView Object

## Description

PresentationSnapshotView object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Edit](../PresentationSnapshotView/PresentationSnapshotView_Edit.md) | Method that enters the presentation snapshot view edit mode. Currently the edit(or even for some query functions) out of edit mode for snapshot view is not allowed. |
| [ExitEdit](../PresentationSnapshotView/PresentationSnapshotView_ExitEdit.md) | Method that exits the presentation snapshot view edit mode. |
| [SetAppearance](../PresentationSnapshotView/PresentationSnapshotView_SetAppearance.md) | Method that sets override appearance. This is applicable to the leaf component. |
| [SetOpacity](../PresentationSnapshotView/PresentationSnapshotView_SetOpacity.md) | Method that sets override opacity to PresentationComponent objects. |
| [SetVisibility](../PresentationSnapshotView/PresentationSnapshotView_SetVisibility.md) | Method that sets override visibility to PresentationComponent objects. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PresentationSnapshotView/PresentationSnapshotView_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [DisplayName](../PresentationSnapshotView/PresentationSnapshotView_DisplayName.md) | Read-write property that gets and sets the presentation snapshot view name. |
| [Parent](../PresentationSnapshotView/PresentationSnapshotView_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SavedCamera](../PresentationSnapshotView/PresentationSnapshotView_SavedCamera.md) | Read-only property that returns the saved camera for current presentation snapshot view. |
| [StoryboardAssociative](../PresentationSnapshotView/PresentationSnapshotView_StoryboardAssociative.md) | Read-write property that gets and sets whether the PresentationSnapshotView is associative with a PresentationStoryboard object. This is only writable when you set it to False to break the associativity between the storyboard and snapshot view. This shoud be set to False to break the associativity between the snapshot view and sotryboard for editing the snapshot view, otherwise the edit will fail. |
| [Trails](../PresentationSnapshotView/PresentationSnapshotView_Trails.md) | Read-only property that returns the PresentationTrails collection object. |
| [Type](../PresentationSnapshotView/PresentationSnapshotView_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[PresentationScene.ActiveSnapshotView](../PresentationScene/PresentationScene_ActiveSnapshotView.md), [PresentationSnapshotViews.Item](../PresentationSnapshotViews/PresentationSnapshotViews_Item.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |