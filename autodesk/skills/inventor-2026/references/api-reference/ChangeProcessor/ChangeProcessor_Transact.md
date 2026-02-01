# ChangeProcessor.Transact Property

Parent Object: [ChangeProcessor](../ChangeProcessor/ChangeProcessor.md)

## Description

Gets and sets whether to execute the change process as a transacting one. A non-transacting change process cannot be undone or redone.

## Remarks

When set to non-transacting change processor, the changes in the change processor should only include document settings, application options.

## Syntax

ChangeProcessor.**Transact**() As Boolean

## Property Value

This is a read/write property whose value is a Boolean.

## Version

Introduced in version 10
