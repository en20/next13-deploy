from api.adapters.outbound.database.models.run import Run as RunSchema
from api.domain.entities.run import Run
from api.domain.repositories.IRunRepository import IRunRepository
from django.core.exceptions import ObjectDoesNotExist


# Concrete Implementation for Run Repository
class RunRepository(IRunRepository):
    def create(self, task: str, robot: str, status: str) -> Run:
        return self.schemaToRun(
            RunSchema.objects.create(
                task=task,
                robot=robot,
                status=status,
            )
        )

    def update(self, id: str, task: str, robot: str, status: str) -> bool:
        try:
            RunSchema.objects.filter(id=id).update(
                robot=robot,
                task=task,
                status=status,
            )
            return True
        except ObjectDoesNotExist:
            return False

    def delete(self, id) -> bool:
        try:
            RunSchema.objects.filter(id=id).delete()
            return True
        except ObjectDoesNotExist:
            return False

    def findById(self, id) -> Run:
        try:
            return self.schemaToRun(RunSchema.objects.get(id=id))
        except ObjectDoesNotExist:
            return None

    def findAll(self, skip, limit) -> list[Run]:
        return list(map(self.schemaToRun, RunSchema.objects.all()[skip:limit]))

    def getRobotRuns(self, robotId) -> list[Run]:
        return list(map(self.schemaToRun, RunSchema.objects.filter(robot=robotId)))

    def countRobotRuns(self, robotId) -> int:
        return RunSchema.objects.filter(robot=robotId).count()

    def schemaToRun(self, schema: RunSchema) -> Run:
        return Run(
            schema.id, schema.robot.id, schema.task.id, schema.status, str(schema.created_at)
        )
