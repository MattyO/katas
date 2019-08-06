class Bowling():
    def score(self, frames):
        return sum([sum(frame) for frame in frames]) + self.extra_score(frames)

    def extra_score(self, frames):
        frames = iter(frames)
        extra_score = 0
        current_frame = next(frames, None)
        next_frame = next(frames, None)
        second_next_frame = next(frames, None)

        while next_frame !=  None:
            if current_frame[0] != 10 and sum(current_frame) == 10:
                extra_score += next_frame[0]

            if current_frame[0] == 10:
                next_throws = list(filter(lambda x: x != 0, next_frame + second_next_frame))
                extra_score += next_throws[0] + next_throws[1]

            current_frame = next_frame
            next_frame = next(frames, None)

        return extra_score
